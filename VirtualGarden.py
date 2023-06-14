import time

class VirtualGarden:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def water_plants(self):
        print("Watering the plants...")
        for plant in self.plants:
            print("Watering", plant)
            time.sleep(1)
        print("All plants watered.")

def main():
    garden = VirtualGarden()

    # Add plants to the virtual garden
    garden.add_plant("Rose")
    garden.add_plant("Sunflower")
    garden.add_plant("Tulip")
    garden.add_plant("Lily")

    # Water the plants
    garden.water_plants()

if __name__ == "__main__":
    main()
