from observer_interface import FitnessDataObserver

class LiveActivityDisplay(FitnessDataObserver):
    def update(self, fitness_data):
        # print(f"LiveActivityDisplay: Steps: {fitness_data.step}, "
        #       f"Calories: {fitness_data.calories_burned:.1f}, "
        #       f"Distance: {fitness_data.distance_covered:.2f} km")
        print("Liveactivity done")
        print(fitness_data.step)