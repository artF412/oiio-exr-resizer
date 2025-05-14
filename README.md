# 🎞️ Resize EXR

A simple Python tool for batch resizing `.exr` files using `oiiotool`.

---

## 📥 Installation Guide

### 1. 🔧 Install oiiotool

```bash
sudo apt update
sudo apt install openimageio-tools -y
```

### 2. 📦 Clone the Repository

```bash
git clone https://github.com/artF412/Resize_EXR.git
cd Resize_EXR
```

---

## 🚀 Usage

```bash
python main.py <input_folder> <output_folder> <size>
```

### Example
```bash
python main.py ./input_exr ./output_exr 1920x1080
```

---

### 📌 Argument Descriptions

- `<input_folder>`: Folder containing the `.exr` files to be resized  
- `<output_folder>`: Folder to save the resized `.exr` files  
- `<size>`: New image resolution in the format `WIDTHxHEIGHT`, e.g., `1920x1080`

---

### ⚠️ Notes

- The size **must use the letter `x`**, not `*`, e.g., `4000x2000`
- Make sure `oiiotool` is in your `$PATH` by running:
  ```bash
  which oiiotool
  ```
- If you encounter an error like `std::bad_alloc`, it may be due to the image size exceeding your system’s memory capacity

---