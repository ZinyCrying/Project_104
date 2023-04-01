import cv2 

img = cv2.imread("solar-system.jpg")

#print(img)

cv2.putText(
    img,
    "Sun",
    [60,40],
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (0,0,255)
    )

cv2.putText(
    img,
    "Mercury",
    [110,180],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.putText(
    img,
    "Venus",
    [190,260],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.putText(
    img,
    "Earth",
    [290,150],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.putText(
    img,
    "Mars",
    [385,260],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.putText(
    img,
    "Jupiter",
    [580,50],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.putText(
    img,
    "Saturn",
    [750,300],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.putText(
    img,
    "Uranus",
    [965,140],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.putText(
    img,
    "Neptune",
    [1105,285],
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
    )

cv2.imshow("solar system", img)

cv2.waitKey(0)

