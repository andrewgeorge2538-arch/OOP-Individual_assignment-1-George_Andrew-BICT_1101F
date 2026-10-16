from models import Farm, CropRecord, SUPPORTED_CROPS


def add_farm(farms, farm):
    if farm.farm_id in farms:
        print("That farm ID already exists.")
        return False
    farms[farm.farm_id] = farm
    return True


def display_farms(farms):
    if not farms:
        print("No farms have been added yet.")
        return
    for farm in farms.values():
        farm.display_info()


def read_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a number greater than 0.")


def menu_add_farm(farms):
    text = input("Enter farm as ID,District,Chiefdom (e.g. F001,Bo,Tikonko): ")
    farm = Farm.from_text(text)
    if farm is None:
        print("Invalid format. Please try again.")
    elif add_farm(farms, farm):
        print(f"Farm {farm.farm_id} added.")


def menu_add_record(farms):
    farm_id = input("Farm ID: ").strip().upper()
    if farm_id not in farms:
        print("Farm not found. Add the farm first.")
        return

    crop = input(f"Crop ({', '.join(SUPPORTED_CROPS)}): ").strip()
    if not CropRecord.is_valid_crop(crop):
        print("Crop not supported.")
        return

    season = input("Season (e.g. 2026-Rainy): ").strip()
    if not season:
        print("Season is required.")
        return
    area = read_number("Area planted (hectares): ")
    harvest = read_number("Harvest (kg): ")

    record = CropRecord(crop, season, area, harvest)
    farms[farm_id].add_record(record)
    print(f"Record saved. Yield: {record.yield_per_ha():.1f} kg/ha")


def main():
    farms = {}
    print("=== Crop Yield Monitoring System ===")
    while True:
        print("\n1. Add farm\n2. Add harvest record\n3. View all farms\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            menu_add_farm(farms)
        elif choice == "2":
            menu_add_record(farms)
        elif choice == "3":
            display_farms(farms)
        elif choice == "4":
            print(f"Goodbye. Records saved this session: {CropRecord.get_record_count()}")
            break
        else:
            print("Invalid option. Choose 1 to 4.")


if __name__ == "__main__":
    main()
