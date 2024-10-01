import time
import streamlit as st

class WorkTracker:

    def __init__(self,age,category,level,frequency):
        self.age = age
        self.category = category
        self.level = level
        self.frequency = frequency
        self.rest_of_set =self.time_of_set =self.no_of_set=self.rest_of_workout=0


    def AlreadyDefSetRepSorted(self):
        workouts = {
            1: { "name": "STRENGTH WORKOUT",
                "exercise":{"Squats (Lower Body)","Deadlifts (Lower Back, Legs, Core)","Bench Press (Upper Body)","Overhead Press (Upper Body)"},
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 12, "rep_time": 40,
                    "rest_between_sets": 60, "rest_between_workouts": 120},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 10, "rep_time": 45,
                    "rest_between_sets": 90, "rest_between_workouts": 150},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 8, "rep_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 180}
            },
            2: {  "name": "CARDIO WORKOUT",
                "exercise": {"Jumping Jacks", "High Knees", "Burpees",
                             "Mountain Climbers"},
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 30, "rep_time": 60,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 20, "rep_time": 75,
                    "rest_between_sets": 120, "rest_between_workouts": 150},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 15, "rep_time": 90,
                    "rest_between_sets": 150, "rest_between_workouts": 180}
            },
            3: {  "name": "FLEXIBILITY WORKOUT",
                "exercise": {"Standing Hamstring Stretch", "Seated Forward Bend", "Butterfly Stretch",
                             "Cat-Cow Stretch"},
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 10, "rep_time": 30,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 8, "rep_time": 40,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 6, "rep_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            4: {  "name": "MOBILITY WORKOUT",
                "exercise": {"Cat-Cow Stretch", "Hip Flexor Stretch", "World’s Greatest Stretch",
                             "Thoracic Spine Rotations"},
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 10, "rep_time": 30,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 8, "rep_time": 40,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 6, "rep_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            5: {  "name": "BODYWEIGHT WORKOUT",
                "exercise": {"Cat - Cow Stretch", "Hip Flexor Stretch", "World Greatest Stretch","Thoracic Spine Rotations"},
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 12, "rep_time": 35,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 10, "rep_time": 40,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 8, "rep_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            6: {  "name": "YOGA WORKOUT",
                "exercise": {"Mountain Pose (Tadasana)", "Downward-Facing Dog (Adho Mukha Svanasana)", "Warrior II (Virabhadrasana II)",
                             "Child's Pose (Balasana)"},
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 5, "rep_time": 60,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 5, "rep_time": 75,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 5, "rep_time": 90,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            7: {  "name": "POWER LIFTING",
                "exercise": {"Squat", "Bench Press","Deadlift",
                             "Overhead Press (Standing Barbell Press)"},
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 5, "rep_time": 45,
                    "rest_between_sets": 120, "rest_between_workouts": 180},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 5, "rep_time": 60,
                    "rest_between_sets": 150, "rest_between_workouts": 180},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 3, "rep_time": 75,
                    "rest_between_sets": 180, "rest_between_workouts": 240}
            },
            8: {  "name": "HIIT",
                "exercise": {"Burpees", "Jump Squats", "Mountain Climbers",
                             "High Knees"},
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 15, "rep_time": 45,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 12, "rep_time": 60,
                    "rest_between_sets": 120, "rest_between_workouts": 150},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 10, "rep_time": 75,
                    "rest_between_sets": 150, "rest_between_workouts": 180}
            },
            9: {  "name": "CORE WORKOUT",
                "exercise": {"Plank", "Russian Twists", "Bicycle Crunches",
                             "Leg Raises"},
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 15, "rep_time": 40,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 12, "rep_time": 45,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 10, "rep_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            10: {  "name": "LOW IMPACT WORKOUT",
                "exercise": {"Bodyweight Squats", "Marching in Place", "Step-Ups",
                             "Seated Leg Extensions"},
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 12, "rep_time": 30,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 10, "rep_time": 35,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 8, "rep_time": 40,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            }
        }

        plan = workouts[self.category][self.level]
        st.markdown("\nYour Workout Plan for Today:")
        st.warning(f"NAME OF THE WORKOUT:**{workouts[self.category]['name']}**")
        st.error(f"Number of Different Exercises: **{plan['workout_count']}**")
        st.info(f"Names of Different Exercises For : **{workouts[self.category]['exercise']}**")
        st.warning(f"Number of Sets per Exercise: **{plan['sets']}**")
        st.success(f"Reps per Set: **{plan['reps_per_set']}**")
        st.warning(f"Time per set: **{plan['rep_time']}** seconds")
        st.info(f"Rest Time between Sets: **{plan['rest_between_sets']}** seconds")
        st.success(f"Rest Time between Workouts: **{plan['rest_between_workouts']}** seconds")

        choseDef = st.selectbox("\nDO YOU WANT TO STICK ON WITH THIS PLAN:", ["Yes", "No"])
        if choseDef == "Yes":
            self.no_of_workout = plan['workout_count']
            self.no_of_set = plan['sets']
            self.no_of_rep = plan['reps_per_set']
            self.time_of_set = plan['rep_time']
            self.rest_of_set = plan['rest_between_sets']
            self.rest_of_workout = plan['rest_between_workouts']
            self.mode = 0
        elif choseDef == "No":
            self.CustomWorkoutTracker()

    def CustomWorkoutTracker(self):
        st.success("\nHOW DO YOU WANT TO SET YOUR TRACKER AND COMPLETE WORKOUT.\n WITHIN A TIME OR BY COMPLETING A NUMBER OF WORKOUTS.")

        mode = st.radio("CHOOSE THE MODE FROM ABOVE : ",
                        ["COMPLETE WORKOUT WITHIN A TIME.",
                         "COMPLETE WORKOUT BY COMPLETING A NUMBER OF WORKOUTS."])
        self.mode = mode

        if self.mode == "COMPLETE WORKOUT WITHIN A TIME.":
            self.mode == 1
            self.timelimit = st.number_input("ENTER THE TIME LIMIT IN MINUTES", min_value=1.0)
            self.noofset = st.number_input("ENTER THE NUMBER OF SETS PER WORKOUT", min_value=1)
            self.noofrep = st.number_input("ENTER THE NUMBER OF REPS PER SET", min_value=1)
            self.timeofset = st.number_input("ENTER THE TIME TAKEN FOR EACH SET IN SECONDS", min_value=1)
            self.restofset = st.number_input("ENTER THE REST TIME AFTER EACH SET IN SECONDS", min_value=1)
            self.restofworkout = st.number_input("ENTER THE REST TIME AFTER EACH WORKOUT IN SECONDS", min_value=1)

        elif self.mode == "COMPLETE WORKOUT BY COMPLETING A NUMBER OF WORKOUTS.":
            self.mode == 2
            self.no_of_workout = st.number_input("ENTER THE NUMBER OF WORKOUTS YOU PLAN TO DO ", min_value=1)
            self.no_of_set = st.number_input("ENTER THE NUMBER OF SETS PER WORKOUT", min_value=1)
            self.no_of_rep = st.number_input("ENTER THE NUMBER OF REPS PER SET", min_value=1)
            self.time_of_set = st.number_input("ENTER THE TIME TAKEN FOR EACH SET IN SECONDS", min_value=1)
            self.rest_of_set = st.number_input("ENTER THE REST TIME AFTER EACH SET IN SECONDS", min_value=1)
            self.rest_of_workout = st.number_input("ENTER THE REST TIME AFTER EACH SET IN SECONDS", min_value=1,key="rest_time_input")

    def trackCalculator(self):
        timeOfEachSet = self.time_of_set + self.rest_of_set
        timeOfEachWorkout = (timeOfEachSet * self.no_of_set) + self.rest_of_workout

        if self.mode == 2 or self.mode == 0:
            totalTimeNeeded = timeOfEachWorkout * self.no_of_workout
            self.total_time_needed_workout = totalTimeNeeded
            minutesToComplete = totalTimeNeeded // 60
            remsecondsToComplete = totalTimeNeeded % 60
            st.info(f"\nYOU CAN COMPLETE THE WORKOUT IN APPROXIMATELY: **{minutesToComplete}** MINUTES AND **{remsecondsToComplete}** SECONDS.")

        elif self.mode == 1:
            totalNumberOfWorkout = (self.time_limit * 60) // timeOfEachWorkout
            self.total_number_of_workout = totalNumberOfWorkout
            st.success(f"\nYOU CAN COMPLETE APPROXIMATELY **{totalNumberOfWorkout}** WORKOUT WITHIN YOUR SPECIFICATIONS.")

        start_command = st.selectbox("\nDO YOU WANT TO START YOUR WORKOUT **(YES/NO)**:", ["Yes", "No"])
        if start_command == "No":
            st.success("THANK YOU FOR OPTING OUR TRACKER. FEEL FREE TO USE ANY TIME.")
        elif start_command == "Yes":
            st.success("YOUR WORKOUT PLAN WILL START WITHIN **60** SECONDS.\n START WITH YOUR FIRST SET WHEN START INDICATOR APPEARS.\n"
                  "STOP THE SET WHEN STOP INDICATOR APPEARS AND TAKE REST\n"
                  "START WITH NEXT SET AFTER SET BREAK. THANK YOU.")
            self.starTrackAlong()

    def starTrackAlong(self):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.6)
            progress_bar.progress(i + 1)

        if self.mode == 0 or self.mode == 2:
            c = 1
            while c < self.no_of_workout +1:
                st.error(f"\nWORKOUT **{c}** WILL START NOW. YOU CAN START ONCE START INDICATOR APPEARS.IN 5sec")
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)

                for i in range(1,self.no_of_set+1):
                    st.info(f"\nSTART SET **{i}** TIME={self.time_of_set}sec")
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(self.time_of_set/10)  # Sleep for 0.1 seconds
                        progress_bar.progress(i + 1)

                    st.error(f"STOP SET**{i}**, TAKE REST TIME={self.rest_of_set}sec")
                    if i < self.no_of_set:
                        progress_bar = st.progress(0)
                        for i in range(100):
                            time.sleep(self.rest_of_set / 10)  # Sleep for 0.1 seconds
                            progress_bar.progress(i + 1)

                if c< self.no_of_workout:
                    st.info(f"WORKOUT **{c}** COMPLETED, TAKE REST FOR {self.rest_of_workout}sec AND CONTINUE WITH NEXT WORKOUTS.")
                elif c>= self.no_of_workout:
                    st.write(f"WORKOUT **{c}** COMPLETED, TAKE REST FOR {self.rest_of_workout}sec AND YOU CAN LEAVE ONCE WORKOUTS COMPLETED DISPLAYS.")
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(self.rest_of_workout / 10)  # Sleep for 0.1 seconds
                    progress_bar.progress(i + 1)
                c += 1

            st.success("**ALL WORKOUTS COMPLETED. GREAT JOB!**")

        elif self.mode == 1:
            t = 1
            while t < self.total_number_of_workout + 1:
                st.write(f"\nWORKOUT **{t}** WILL START NOW IN 5sec. YOU CAN START ONCE START INDICATOR APPEARS.")
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.05)  # Sleep for 0.1 seconds
                    progress_bar.progress(i + 1)
                # time.sleep(5)

                for i in range(1, self.no_of_set + 1):
                    st.warning(f"START SET {i} ,TIME={self.time_of_set} sec")
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(self.time_of_set / 10)  # Sleep for 0.1 seconds
                        progress_bar.progress(i + 1)
                    # time.sleep(self.time_of_set)
                    st.error(f"STOP SET**{i}**, TAKE REST FOR {self.rest_of_set}sec\n")
                    if i < self.no_of_set:
                        progress_bar = st.progress(0)
                        for i in range(100):
                            time.sleep(self.rest_of_set / 10)  # Sleep for 0.1 seconds
                            progress_bar.progress(i + 1)
                        # time.sleep(self.rest_of_set)
                if t < self.total_number_of_workout:
                    st.warning(f"WORKOUT **{t}** COMPLETED, TAKE REST FOR {self.rest_of_workout}sec AND CONTINUE WITH NEXT WORKOUTS.")
                elif t >= self.total_number_of_workout:
                    st.warning(f"WORKOUT **{t}** COMPLETED, TAKE REST FOR {self.rest_of_workout}sec AND YOU CAN LEAVE ONCE WORKOUTS COMPLETED DISPLAYS.")
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(self.rest_of_workout / 10)  # Sleep for 0.1 seconds
                    progress_bar.progress(i + 1)
                # time.sleep(self.rest_of_workout)
                t += 1

            st.info("ALL WORKOUTS COMPLETED. GREAT JOB!")


st.title("HELLO , WELCOME TO YOUR PERSONALIZED WORKOUT HELPER")
Name = st.text_input("Enter your name : ")
age = st.number_input("Enter your Age : ", min_value=1)
category = st.selectbox("Choose Category:", [
    "Strength Workout", "Cardio Workout", "Flexibility Workout", "Mobility Workout",
    "Bodyweight Workout", "Yoga Workout", "Power Lifting", "HIIT", "Core Workout", "Low Impact Workout"
])

category_mapping = {
    "Strength Workout": 1, "Cardio Workout": 2, "Flexibility Workout": 3,
    "Mobility Workout": 4, "Bodyweight Workout": 5, "Yoga Workout": 6,
    "Power Lifting": 7, "HIIT": 8, "Core Workout": 9, "Low Impact Workout": 10
}

category_num = category_mapping[category]

st.write("\nWHICH LEVEL YOU ARE CURRENTLY IN")
level = st.selectbox("Choose Level:", ["BEGINNER", "INTERMEDIATE", "ADVANCED"])

level_mapping = {"BEGINNER": 1, "INTERMEDIATE": 2, "ADVANCED": 3}
level_num = level_mapping[level]

frequency = st.number_input("How often do you work out in a week?", min_value=1)


p1 = WorkTracker(age, category_num, level_num, frequency)
p1.AlreadyDefSetRepSorted()
p1.trackCalculator()
