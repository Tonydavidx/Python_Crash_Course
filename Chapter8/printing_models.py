# unfinished_models = ['phone case', 'bottle', 'cube']
# finsihed_models = []

# while unfinished_models:
#     current_design = unfinished_models.pop()
#     print(f"{current_design} is in print right now") 
#     finsihed_models.append(current_design)

# print("\nthe following models have been printed")
# for fm in finsihed_models:
#     print(fm)

def print_models(unfinished_models,finsihed_models):
    while unfinished_models:
        current_model = unfinished_models.pop()
        print(f"model in print is: {current_model}")
        finsihed_models.append(current_model)

def printed_models(finsihed_models):
    print("\nthese are the models printed: ")
    for fm in finsihed_models:
        print(fm)      

unfinished_models = ['phone case','charger','cube']
finsihed_models = []

print_models(unfinished_models[:],finsihed_models)
printed_models(finsihed_models)

