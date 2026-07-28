# Problem Set 6: pdb Debug Report — GPS Plotter Bug

## The Bug

In `gps_points.txt`, **line 412** contains a corrupted latitude value:

```
95.987111697115196,10.303389172138218
```

| Field | Value | Valid Range | Status |
|---|---|---|---|
| Latitude | **95.99** | [-90, 90] | ❌ OUT OF BOUNDS |
| Longitude | 10.30 | [-180, 180] | ✅ Valid |

A latitude of 95.99 degrees is **outside the Earth's bounds** — the maximum
is 90 degrees at the poles. Without the validation filter, this point would
be plotted far above the Arctic, outside the map extent.

Additionally, **line 480** contains a NaN latitude:
```
nan,120.9992465405
```

## How the Filter Prevents the Bug

In `gps-plotter.py`, the `load_gps_data()` function (lines 20–22) has a filter:

```python
if math.isnan(lat) or abs(lat) > 90 or abs(lon) > 180:
    continue
```

This correctly catches both problematic lines:
- Line 412: `abs(95.99) > 90` → True → filtered
- Line 480: `math.isnan(nan)` → True → filtered

## Debugging with pdb

### Step-by-step in Colab terminal

```bash
!python -m pdb gps-plotter.py
```

```
(Pdb) b 21                          # break at the filter line
Breakpoint 1 at gps-plotter.py:21
(Pdb) c                             # continue until breakpoint
> gps-plotter.py(21)load_gps_data()
-> if math.isnan(lat) or abs(lat) > 90 or abs(lon) > 180:
(Pdb) p line_num                    # (would need a counter variable)
(Pdb) p lat, lon
(95.9871116971152, 10.303389172138218)
(Pdb) p abs(lat) > 90
True                                 # ← THE BUG: latitude 95.99 > 90
(Pdb) n                             # step to next line
> gps-plotter.py(22)load_gps_data()
-> continue                         # skips this invalid point
```

### Conditional breakpoint approach

```bash
(Pdb) b 21, abs(lat) > 90          # break only when latitude is invalid
Breakpoint 1 at gps-plotter.py:21
(Pdb) c
> gps-plotter.py(21)load_gps_data()
-> if math.isnan(lat) or abs(lat) > 90 or abs(lon) > 180:
(Pdb) p lat
95.9871116971152                     # Caught the invalid latitude!
```

## Evidence of Data Corruption

Compare line 412 with a nearby valid line (475):

| Line | Latitude | Longitude |
|---|---|---|
| 412 | **95**.987111697115196 | 10.303389172138218 |
| 475 | **6**.987111697115196 | -50.0204112721442 |

The fractional parts `.987111697115196` are **identical**, suggesting that
line 412's latitude is a corrupted version of the correct value `6.987...`.
The digit `6` was somehow replaced with `95`.

## Conclusion

- **Root cause**: Corrupted latitude value at line 412 (95.99 degrees)
- **Why it matters**: Without the filter, it would plot far outside the map
- **Fix in place**: The validation filter in `load_gps_data()` catches it
- **Lesson**: Always validate input data — GPS latitude MUST be in [-90, 90]
