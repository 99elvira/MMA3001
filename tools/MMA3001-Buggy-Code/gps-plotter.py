import math
import matplotlib.pyplot as plt
from PIL import Image

# --- Step 1: Load and filter data ---
def load_gps_data(filename="gps_points.txt"):
    """Loads GPS data from a file, filters invalid points, and returns valid coordinates.

    Args:
        filename (str, optional): The path to the GPS data file. Defaults to "gps_points.txt".

    Returns:
        list[tuple[float, float]]: A list of (latitude, longitude) tuples for valid GPS points.
            Invalid points (NaN latitude, latitude > 90, or longitude > 180) are skipped.
    """
    coords = []
    with open(filename) as f:
        for line in f:
            lat, lon = line.strip().split(',')
            lat, lon = float(lat), float(lon)
            if math.isnan(lat) or abs(lat) > 90 or abs(lon) > 180:
                continue
            coords.append((lat, lon))
    return coords

# --- Step 2: Plot on world map ---
def plot_gps_points(coords, map_image="Plate-Carree-Projection.png"):
    """Plots a list of GPS coordinates on a world map image.

    Args:
        coords (list[tuple[float, float]]): A list of (latitude, longitude) tuples to plot.
        map_image (str, optional): The path to the world map image file. Defaults to "Plate-Carree-Projection.png".

    Raises:
        FileNotFoundError: If the `map_image` file is not found.

    Returns:
        None: Displays the plot using matplotlib.
    """
    img = Image.open(map_image)
    plt.imshow(img, extent=[-180, 180, -90, 90])
    lats, lons = zip(*coords)
    plt.scatter(lons, lats, c='red', s=10)
    #plt.title("GPS Points on World Map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

# --- Run ---
points = load_gps_data()
plot_gps_points(points)
