import os

train_cats = "dataset/train/cats"
train_no_cats = "dataset/train/not_cats" 
val_cats = "dataset/val/cats"
val_no_cats = "dataset/val/not_cats" 

image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

image_count_train_cats = sum(1 for file in os.listdir(train_cats) if file.lower().endswith(image_extensions))
image_count_train_no_cats = sum(1 for file in os.listdir(train_no_cats) if file.lower().endswith(image_extensions))
image_count_val_cats = sum(1 for file in os.listdir(val_cats) if file.lower().endswith(image_extensions))
image_count_val_no_cats = sum(1 for file in os.listdir(val_no_cats) if file.lower().endswith(image_extensions))

print(f"Number of train cats: {image_count_train_cats}")
print(f"Number of train not cats: {image_count_train_no_cats}")
print(f"Number of val cats: {image_count_val_cats}")
print(f"Number of val not cats: {image_count_val_no_cats}")