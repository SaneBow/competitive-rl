from car_racing_multi_players import CarRacing

if __name__ == "__main__":
    env = CarRacing(num_player=1)
    # example: env.reset(use_local_track="./track/test.json",record_track_to="")
    # example: env.reset(use_local_track="",record_track_to="./track")
    env.reset(use_local_track="", record_track_to="")
    cnt = 0
    while True:
        env.render()
        # observation, reward, done, info = env.step(env.action_space.sample())
        if cnt < 10:
            observation, reward, done, info = env.step([0, 1])
        if cnt > 10:
            observation, reward, done, info = env.step([0, -1])
            # observation, reward, done, info = env.step([0, 0])  # with the no-brake bug, car's behavior is the same as always setting brake to 0
        cnt += 1
        if cnt == 20:
            cnt = 0
        if env.show_all_car_obs:
            env.show_all_obs(observation)
