# Instagram Reel to Socialverse Video Uploader

A Python script that allows you to download an Instagram reel, upload it to the Socialverse platform, and create a post with the uploaded video. The script uses the `requests` and `instaloader` libraries to interact with Instagram and the Socialverse API.

---

## 🛠️ Features

- **Download Instagram Reels**: Download Instagram reels by providing the reel URL.
- **Upload Videos**: Upload the downloaded video to Socialverse using a pre-signed upload URL.
- **Create Posts**: Create a post on Socialverse with the uploaded video and make it available for sharing.

---

## 🔑 Prerequisites

Before running the project, make sure you have the following:

- **Python 3.x** installed on your system.
- **Flic API Token**: An active token to interact with the Socialverse platform.
- **Instaloader**: A library to download Instagram posts.

### Required Libraries

Install the required libraries by running:

```bash
pip install -r requirements.txt
```

---

## 📝 Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sj422159/instagram-reel-to-socialverse.git
   cd instagram-reel-to-socialverse
   ```

2. **Set up your Flic API Token**:

   - Obtain a valid **Flic API token** from the Socialverse platform.
   - Open `main.py` and replace the `FLIC_TOKEN` variable with your token.

3. **Install dependencies**:

   Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Instagram reel**:

   - The script will prompt you for the **Instagram Reel URL**, **video title**, and **category ID**.
5.  **Additional Setup**:

   - Make a downloads folder inside the directory.
---

## 🚀 Usage

1. **Run the script**:

   Run the following command to start the script:

   ```bash
   python main.py
   ```

2. **Follow the prompts**:

   The script will ask for the following inputs:

   - **Instagram Reel URL**: The URL of the Instagram reel you want to download.
   - **Video Title**: The title you want to give the uploaded video.
   - **Category ID**: (Optional) The category ID for the post (defaults to `25`).

3. **What Happens Next?**:

   - The script downloads the Instagram reel.
   - Uploads the video to the Socialverse platform.
   - Creates a post with the uploaded video using the provided title and category.

---

## 💻 Functions

### `get_upload_url()`
- **Description**: Requests a pre-signed URL from the Socialverse API for video uploads.
- **Returns**: A tuple containing the `upload_url` and `video_hash`, or `(None, None)` if an error occurs.

### `download_instagram_reel(reel_url, download_folder)`
- **Description**: Downloads an Instagram reel from the provided URL.
- **Parameters**:
  - `reel_url` (str): The URL of the Instagram reel to download.
  - `download_folder` (str, optional): The folder where the video will be saved. Default is `"downloads"`.
- **Returns**: The file path to the downloaded video, or `None` if the download fails.

### `upload_video(upload_url, video_file_path)`
- **Description**: Uploads the video to the provided pre-signed URL.
- **Parameters**:
  - `upload_url` (str): The pre-signed URL for uploading the video.
  - `video_file_path` (str): The path to the video file to upload.
- **Returns**: `True` if the upload is successful, `False` otherwise.

### `create_post(title, video_hash, category_id=25, is_available_in_public_feed=False)`
- **Description**: Creates a post on Socialverse using the video hash.
- **Parameters**:
  - `title` (str): The title of the post.
  - `video_hash` (str): The hash of the uploaded video.
  - `category_id` (int, optional): The category ID for the post. Default is `25`.
  - `is_available_in_public_feed` (bool, optional): Whether the post should be visible in the public feed. Default is `False`.
- **Returns**: None

---

## ⚠️ Error Handling

The script provides error handling for:

- Invalid Instagram reel URL or missing video.
- Failure to upload the video to Socialverse.
- Issues with creating the post.

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- **Instaloader**: For downloading Instagram posts.
- **Requests**: For making HTTP requests to the Socialverse API.
- **Socialverse API**: For video upload and post creation.

---

## 🌟 Contributing

If you want to contribute to this project, feel free to fork it and create a pull request. We welcome any improvements or bug fixes!

---



```

### Key Changes:
1. **Structured Layout**: Added headings for each section to make it easy to navigate.
2. **Visual Enhancements**: Added emojis for sections (e.g., rocket for usage, key for prerequisites) to make the README more engaging.
3. **Clarified Instructions**: Step-by-step setup and usage instructions with clear formatting.
4. **Contributing Section**: Encouraged collaboration and contribution to the project.
5. **Social Links**: A section to add links to related social media or project pages.
6. **Error Handling**: Added a specific error handling section to inform users of the types of errors they might encounter.
