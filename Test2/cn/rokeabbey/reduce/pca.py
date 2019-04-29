import numpy as np
import matplotlib.pyplot as mtp
import matplotlib.image as mpimg
gray_cofficient = np.array([0.299, 0.587, 0.114])


def rgb2gray(rgb):
    return rgb[..., :3] @ gray_cofficient


def main():
    pic = mpimg.imread('ord.jpg')
    mtp.figure(1)
    mtp.subplot(2, 2, 1)
    mtp.imshow(pic)
    gray_pic = rgb2gray(pic)
    mtp.subplot(2, 2, 2)
    mean = np.mean(gray_pic.T, axis=1)
    mean.shape = mean.size, 1
    mtp.imshow(gray_pic)
    mean_gray_pic = (gray_pic.T - mean).T
    lmd, P = np.linalg.eig(mean_gray_pic @ mean_gray_pic.T)
    P = np.delete(P, range(30, P.shape[1]), 1)
    new_img = ((P @ P.T @ mean_gray_pic).T + mean).T
    print(lmd)
    print(P)
    print(gray_pic)
    print(new_img)
    # print(new_img.shape)
    mtp.subplot(2, 2, 3)
    mtp.imshow(new_img)
    mtp.show()


if __name__ == '__main__':
    main()

