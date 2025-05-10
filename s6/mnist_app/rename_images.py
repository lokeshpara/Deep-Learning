import os

def rename_images():
    images_dir = os.path.join('static', 'images')
    rename_map = {
        'test accuracy.png': 'test_accuracy.png',
        'test loss.png': 'test_loss.png',
        'L1 misclassified images.png': 'l1_misclassified.png',
        'L2 misclassified images.png': 'l2_misclassified.png'
    }
    
    for old_name, new_name in rename_map.items():
        old_path = os.path.join(images_dir, old_name)
        new_path = os.path.join(images_dir, new_name)
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"Renamed {old_name} to {new_name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {str(e)}")
        else:
            print(f"File not found: {old_name}")

if __name__ == '__main__':
    rename_images() 