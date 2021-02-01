def print_models(unfinished_models,finsihed_models):
    while unfinished_models:
        current_model = unfinished_models.pop()
        print(f"model in print is: {current_model}")
        finsihed_models.append(current_model)

def printed_models(finsihed_models):
    print("\nthese are the models printed: ")
    for fm in finsihed_models:
        print(fm)   