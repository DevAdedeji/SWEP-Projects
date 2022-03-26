#A program to calculate the volume and area of a sphere 
#formula for volume is (4*pi*r^3)/3
#formula for area is 4*pi*r^2

def volume_sphere(radius):
    volume_of_sphere = (4 * (22/7) * (radius ** 3)) / 3
    print("The volume of the sphere is", volume_of_sphere)
def area_sphere(radius):    
    area_of_sphere = 4 * (22/7) * (radius ** 2)
    print("The area of the sphere is", area_of_sphere, '\n')



list_of_radius = [1,6,12.2, 0.2]

for i in list_of_radius:
    volume_sphere(i)
    area_sphere(i)

