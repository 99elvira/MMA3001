import numpy as np

# function to load case 1
def case(num):
  """
  Function to load A,b matrices and arrays for sample linear systems.
    
  Args:
      num (int): the case number.

  Returns:
      A (np.ndarray): A 2D array of shape (N, N) containing float values.
      b (np.ndarray): A 1D array of shape (N) containing float values.
  """
  try:
    A = np.load(f'cases/A{num}.npy')
  except:
    print(f"File A{num}.npy not found!")
  try:
    b = np.load(f'cases/b{num}.npy')
  except:
    print(f"File b{num}.npy not found!")

  return A,b
  
