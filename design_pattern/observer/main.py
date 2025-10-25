from fitness_data import FitnessData
from live_activity_display import LiveActivityDisplay

def main():
    print("################### Demostrating Observer Design Pattern")

    fitness_data = FitnessData()
    liveactivityDisplay = LiveActivityDisplay()

    # ADD the observer

    fitness_data.RegisterObserver(liveactivityDisplay)

    print("\n--- Fitness Data Updated ---")
    fitness_data.set_fitness_data(5000, 250.0, 3.2)


if __name__ == "__main__":
    main()
