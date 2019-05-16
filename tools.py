import cv2
from tqdm import tqdm



def video2Img(pathVideo, pathVideoDestination):
  '''
  Permet d'enregistrer des frames a partir d'un vidéo
  :param pathVideo: chemin de la video d'origine
  :param pathVideoDestination: chemin de destination pour les frames
  :return:
  '''
  vidcap = cv2.VideoCapture(pathVideo)
  success,image = vidcap.read()

  for count in tqdm(range(int(vidcap.get(7))), "Conversion de la video : '{}'".format(pathVideo)):
    cv2.imwrite(pathVideoDestination + "frame%d.jpg" % count, image)
    success,image = vidcap.read()



if __name__ == "__main__":
  """
  # MAIN
  """
  pathVideoOrigin = "C:\\Users\\Utilisateur\\Desktop\\Test video\\video\\video.mp4"
  pathVideoDestination ="C:\\Users\\Utilisateur\\Desktop\\Test video\\image\\"
  video2Img(pathVideoOrigin, pathVideoDestination)
