class Coordinate:
  def __init__(self, value_x, value_y):
    self.x = value_x
    self.y = value_y
  
  def get_coordinates(address):
    try:
        location = Nominatim(user_agent="EdwinTrident").geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return (None, None)
    except Exception as e:
        print(f"Error: {e}")
        return (0, 0)
  
  #Belgiums latitude is in the 49-52 range
  @staticmethod
  def fix_coordinates_lat(x_given):
    while x_given > 100:
      x_given = x_given/10.
    return x_given 

  #Belgians longitude is in the 4-7 range
  @staticmethod
  def fix_coordinates_long(y_given):
    while y_given > 10:
      y_given = y_given/10.
    return y_given