from pdf2image import convert_from_path
from random import SystemRandom
from string import ascii_letters, digits
import os

FILE_NAME_SIZE = 5
UPLOAD_PATH = "uploads"
def convert_and_save(filename:str) -> str:
    images = convert_from_path(filename)
    new_folder = ''.join(SystemRandom().choice(ascii_letters + digits) for _ in range(FILE_NAME_SIZE))
    os.mkdir(f"{UPLOAD_PATH}/{new_folder}")
    for i, image in enumerate(images):
        image.save(f"{UPLOAD_PATH}/{new_folder}/{i}.jpg", "JPEG")
    return new_folder


def main():
    images = convert_from_path("Project Proposal.pdf")
    for i, image in enumerate(images):
        image.save(f"slide_{i}.jpg", "JPEG")


if __name__ == '__main__':
    main()