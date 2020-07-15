import random

adjectives_list = ['clear', 'wicked', 'angry', 'rebel', 'long', 'complete', 'quiet', 'stingy', 'dizzy', 'clean', 'stale', 'scary', 'weary', 'puffy', 'merciful', 'hellish', 'wasteful', 'red','handsome', 'big', 'fit', 'level', 'pale', 'premium', 'fine', 'exotic',
                   'ultra', 'better', 'cute', 'empty', 'wise', 'panoramic', 'rainy', 'faulty', 'dusty','literate', 'greedy', 'bloody', 'fresh', 'massive', 'unarmed', 'anxious', 'many', 'petite', 'awful', 'dull', 'unequal', 'feeble', 'gorgeous', 'uppity', 'huge', 'curly', 'elderly', 'closed', 'mindless', 'marked', 'useful', 'dirty', 'rigid', 'gray', 'jolly', 'brave', 'joyous', 'vast', 'lovely', 'drunk', 'nosy', 'elite', 'bumpy', 'cultured', 'living', 'fragile', 'sore', 'cheap', 'tasteless', 'nice', 'shy', 'broad',
                   'crabby', 'fat', 'odd', 'low', 'caring', 'glorious', 'short', 'silent', 'stupid', 'bald',
                   'amused', 'thick', 'like', 'smooth', 'feigned', 'rotten', 'chunky', 'harsh', 'sneaky', 'ten',
                   'pretty', 'old', 'yellow', 'gentle', 'tense', 'versed', 'open', 'chill', 'wary', 'strong',
                   'smelly', 'original', 'present', 'square', 'furry', 'nasty', 'bashful', 'dapper', 'impossible',
                   'average', 'messy', 'curious', 'sassy', 'easy', 'crowded', 'majestic', 'spiteful', 'standing',
                   'free', 'calm', 'tasty', 'shallow', 'delicious', 'smiling', 'royal', 'tough',
                   'filthy', 'precious', 'healthy', 'relieved', 'terrific', 'strange', 'ready', 'rare', 'secret',
                   'addicted', 'discreet', 'fast', 'bright', 'slim', 'dark', 'legal', 'sincere', 'mere', 'quick',
                   'flaky', 'burnt', 'purple', 'white', 'small', 'cool', 'slow', 'spiky', 'loud',
                   'cruel', 'serious', 'boring', 'silly', 'young', 'pink', 'vulgar', 'prickly', 'gainful', 'godly',
                   'idiotic', 'five', 'damaged', 'mushy', 'melted', 'naughty', 'foolish', 'black', 'goofy', 'tiny',
                   'same', 'hot', 'warm', 'stiff', 'lush', 'plump', 'cold', 'chubby', 'loose',
                   'brainy', 'jazzy', 'vague', 'halting', 'classy', 'nervous', 'cuddly', 'soft']

names_list = ['root', 'dinner', 'town', 'trains', 'touch', 'shoe', 'jail', 'wealth', 'plot', 'throat', 'corn', 'pest',
              'smile', 'account', 'wound', 'pen', 'trip', 'angle', 'flock', 'tank', 'church', 'giraffe', 'top', 'pipe',
              'doctor', 'dime', 'end', 'oil', 'ball', 'swing', 'neck', 'cherries', 'vegetable', 'mother', 'science',
              'kick', 'ground', 'sleet', 'bells', 'food', 'lamp', 'letters', 'water', 'clock', 'vein', 'motion', 'rice',
              'iron', 'dolls', 'silk', 'lake', 'wood', 'birth', 'quilt', 'crow', 'suit', 'car', 'circle', 'cakes',
              'button', 'flowers', 'screen', 'wool', 'zebra', 'smash', 'cat', 'cow', 'low', 'beds', 'insect', 'blow',
              'horn', 'shape', 'sponge', 'sleep', 'birds', 'street', 'talk', 'dad', 'ice', 'houses', 'wash', 'picture',
              'card', 'jump', 'calendar', 'plants', 'sky', 'coach', 'hand', 'shop', 'amount', 'money', 'boots', 'cover',
              'cat', 'bear', 'tray', 'lunch', 'mouth', 'fruit', 'rod', 'plate', 'cable', 'flight', 'van', 'cannon',
              'dog', 'minister', 'teeth', 'feet', 'mist', 'carrot', 'pollution', 'pin', 'cheese', 'wax', 'advice',
              'mine', 'watch', 'hope', 'rifle', 'activity', 'yam', 'earth', 'scent', 'bedroom', 'gum', 'camera',
              'screw', 'gold', 'meat', 'chicken', 'thought', 'cup', 'gate', 'stone', 'rainstorm', 'test', 'smell',
              'quartz', 'throne', 'tree', 'week', 'fork', 'question', 'fairies', 'socks', 'shame', 'view', 'self',
              'phone', 'bath', 'salt', 'chin', 'belief', 'crowd', 'behavior', 'art', 'rat', 'clover', 'fool', 'cart',
              'rabbit', 'board', 'brake', 'step', 'idea', 'relation', 'space', 'weight', 'deer', 'stomach', 'shoes',
              'wave', 'book', 'tongue', 'airplane', 'humor', 'dock', 'hammer', 'baseball', 'finger', 'children', 'star',
              'taste', 'notebook', 'mom', 'pull', 'popcorn', 'veil', 'birthday', 'hair', 'jam', 'battle', 'planes',
              'boat', 'debt', 'business']


# print(random.choice(adjectives_list) + " " + random.choice(names_list))


def randomtoken():
    for i in range(400):
        print(random.choice(adjectives_list) + " " + random.choice(names_list))


randomtoken()
