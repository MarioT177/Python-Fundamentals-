def print_models(car_models, completed_models):

    while car_models:
        current_design = car_models.pop()

        print(f"car make: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


