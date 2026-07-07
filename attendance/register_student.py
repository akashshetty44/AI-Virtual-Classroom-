import cv2
import os

# Folder to save student face images
DATASET_PATH = "attendance/faces"

os.makedirs(DATASET_PATH, exist_ok=True)


def register_student():
    name = input("Enter Student Name: ").strip()

    if not name:
        print("Invalid name!")
        return

    student_folder = os.path.join(DATASET_PATH, name)
    os.makedirs(student_folder, exist_ok=True)

    camera = cv2.VideoCapture(0)

    print("\nPress 's' to capture an image.")
    print("Press 'q' to finish.\n")

    image_count = 0

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Unable to access camera.")
            break

        cv2.putText(
            frame,
            f"Student: {name}",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            "Press S to Save | Q to Quit",
            (20, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2,
        )

        cv2.imshow("Student Registration", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            filename = os.path.join(student_folder, f"{image_count}.jpg")
            cv2.imwrite(filename, frame)
            image_count += 1
            print(f"Saved: {filename}")

        elif key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    print(f"\nRegistration Completed!")
    print(f"Student: {name}")
    print(f"Images Saved: {image_count}")


if __name__ == "__main__":
    register_student()
