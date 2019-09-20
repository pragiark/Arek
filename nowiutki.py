def print_models(
        unprinted_designs, completed_models):
    """printujmey modele"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Wydruk modelu " + current_design)

def show_completed_models(completed_models):
    """wyswietla modele"""
    print("\n Wydrukowane zostały modele :")
    for completed_model in completed_models:
        print(completed_model)

