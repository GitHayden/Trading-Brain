class AgentConfig(object):
    scale = 30
    
    max_step = 600 * scale
    memory_size = 10 * scale
    
    batch_size = 64
    discount = 0.99
    target_q_update_step = 1 * scale
            
    learning_rate_params = {'lr':0.002, 'min':0.0001, 'decay':0.96, 'decay_step':10*scale}
    
    ep_end = 0.00
    ep_start = 1.
    ep_end_t = int(max_step *0.8)
    
    history_length = 1
    train_frequency = 1
    learn_start = 0
        
    double_q = True
    dueling = True
    
    randact = [0.2,0.2,0.6]
    
    test_step = 20 * scale
    
class EnvironmentConfig(object):
    env_name = 'TradingGame'
    num_hidden = 5
    action_size = 3
    max_reward = 16.
    min_reward = -16.
    input_size = 2
    num_st = 5
    amp_scale = 2
    samepenalty = 1.5
    rewardscale = 1.0

class DQNConfig(AgentConfig, EnvironmentConfig):
    pass

def get_config(args):
    if args.model == 'trading':
        config = DQNConfig
    else:
        raise ValueError("Bad model {0}".format(args.model))

    return config
