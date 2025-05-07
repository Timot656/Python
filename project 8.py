import math
def calculate_trigonometric_functions(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    sine = math.sin(angle_radians)
    cosine = math.cos(angle_radians)
    tangent = math.tan(angle_radians)
    return sine, cosine, tangent
angle = 45  
sine, cosine, tangent = calculate_trigonometric_functions(angle)
print(f"Sine({angle}°) = {sine}")
print(f"Cosine({angle}°) = {cosine}")
print(f"Tangent({angle}°) = {tangent}")