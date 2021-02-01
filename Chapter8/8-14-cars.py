def make_car(macnufactuarer,model,**car_info):
    """ create a car profile """
    car_info['maker'] = macnufactuarer
    car_info['model'] = model
    return car_info

car = make_car('bmw','X6',color='white',seats=4)
print(car)

