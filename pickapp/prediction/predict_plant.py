import numpy as np
import tensorflow as tf
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

dir_path = os.path.dirname(os.path.realpath(__file__))
#classes_dict = np.load(dir_path + '/classes_dict.npy', allow_pickle=True).item()
classes_dict = {0: 'African Violet', 1: 'Air Plant ', 2: 'Aloe', 3: 'Aluminum Plant ', 4: 'Amaryllis ', 5: 'Artilliery Plant ', 6: 'Asparagus Fern', 7: 'Bamboo Palm', 8: 'Barrel Cacti', 9: 'Birdnest Fern', 10: 'Boston Fern ', 11: 'Burro’s Tail ', 12: 'Candelabra Cacti', 13: 'Cast Iron Plant ', 14: 'Chin Cacti', 15: 'Chinese Evergreen ', 16: 'Christmas Cacti', 17: 'Creeping Fig ', 18: 'Croton ', 19: 'Cyclamen ', 20: 'Dieffenbachia or Dumbcane ', 21: 'Dragon Lilies ', 22: 'Earth Stars ', 23: 'Easter Cacti', 24: 'English Ivy ', 25: 'Episcia, Flame Violet ', 26: 'False Aralia ', 27: 'Fiddle Leaf Fig ', 28: 'German Ivy ', 29: 
'Grape Ivy', 30: 'Hawaiian Ti', 31: 'Hedgehog cacti', 32: 'Indian Laurel ', 33: 'Jade Plant ', 34: 'Kalanchoe ', 35: 'Kangaroo Ivy ', 36: 'Kentia Palm ', 37: 'Lady Palm ', 38: 'Living Vase', 39: 'Moses in the Cradle ', 40: 'Nerve Plant ', 41: 'Norfolk Island Pine ', 42: 'Pathos', 43: 'Peace Lily ', 44: 'Peacock Plant ', 45: 'Peperomia ', 46: 'Philodendron ', 47: 'Pincushion cacti ', 48: 'Pineapple', 49: 'Ponytail Palm ', 50: 'Prayer Plant ', 51: 'Prickly Pears ', 52: 'Rubber Plant ', 53: 'Schefflera ', 54: 'Snake Plant or Mother', 55: 'Spider Plant ', 56: 'Staghorn Fern', 57: 'Strawberry Geranium ', 
58: 'Swedish Ivy ', 59: 'Sword Fern', 60: 'Thanksgiving Cacti', 61: 'Torch Cacti ', 62: 'Velvet Plant ', 63: 'Wandering Jew ', 64: 'Weeping Fig ', 65: 'Zebra Plant '}
model_file = dir_path+"/sigmoid.h5"
#toxic,MWatering,IWatering,DWatering,Humidity,Light,Temp,LifeSpan,height,Diameter,Sandy,Clay,Silt,Peat,Chalk,Loam,Soil-less
in_features = np.array([0., 1., 0., 0., 33., 5.565331, 53., 0.3485999,
                        49.488686, 25.329721, 1., 0., 0., 0., 0., 0., 0.])

def predict_plant(in_features, classes_dict = classes_dict ,model_file = model_file, thresh=0.2):
    model = tf.keras.models.load_model(model_file)
    preds = model.predict(np.reshape(in_features, (1, -1)))
    plants = [classes_dict[i] for i in np.argwhere(preds >= thresh)[:, 1]]
    probs = list(preds[preds >= thresh])
    return plants, probs

#print(predict_plant(in_features,classes_dict,model_file))


