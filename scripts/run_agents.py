from wrappers import DefaultCameraCar
def trivial_agent():
    env = DefaultCameraCar()
    obs = env.reset()
    while True:
        action = {'ego_idx':0, 'speed':[5.0, 0.0], 'steer':[0.0, 0.0]}
        obs, rew, done, info = env.step(action)
        if done:
            print("DONE")

def fgm_agent():
    from fgm import FGM
    env = DefaultCameraCar()
    obs = env.reset()
    ego_agent = FGM(env.angle_min, env.angle_inc, speed=4.0)
    while True:
        angle, speed = ego_agent.do_FGM(obs['scans'][0])
        action = {'ego_idx':0, 'speed':[speed, 0.0], 'steer':[angle, 0.0]}
        obs, rew, _, info = env.step(action)

trivial_agent()