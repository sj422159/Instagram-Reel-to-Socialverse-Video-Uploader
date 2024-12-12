import requests
import os
import instaloader

# Constants
BASE_URL = "https://api.socialverseapp.com"
FLIC_TOKEN = "flic_0ca6325a4e3c7bc5254757e880dac3d295597c44ba3c5a185e836678cb89bf4d"  # Flic API token

# Step 1: Get a pre-signed upload URL from the API.
def get_upload_url():
    """
    Requests a pre-signed upload URL and video hash from the API to upload a video.

    Returns:
        tuple: (upload_url, video_hash) if successful, else (None, None)
    """
    try:
        # Headers for the request
        headers = {
            "Flic-Token": FLIC_TOKEN,
            "Content-Type": "application/json"
        }
        # Make GET request to fetch upload URL and video hash
        response = requests.get(f"{BASE_URL}/posts/generate-upload-url", headers=headers)

        if response.status_code == 200:
            data = response.json()
            print("Response JSON:", data)  # Debugging: Print the API response
            upload_url = data.get("url")  # Use 'url' instead of 'upload_url' in the response
            video_hash = data.get("hash")

            if upload_url and video_hash:
                print("Pre-signed URL and hash obtained successfully!")
                return upload_url, video_hash
            else:
                print("Error: Missing 'url' or 'hash' in the response.")
                return None, None
        else:
            print(f"Failed to get upload URL. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            return None, None
    except Exception as e:
        print(f"Error getting upload URL: {e}")
        return None, None


# Step 2: Download Instagram reel
def download_instagram_reel(reel_url, download_folder="downloads"):
    """
    Downloads an Instagram reel video and returns the file path.

    Args:
        reel_url (str): The URL of the Instagram reel.
        download_folder (str): The folder to store the downloaded video.

    Returns:
        str: Path to the downloaded video file, or None if download fails.
    """
    loader = instaloader.Instaloader()  # Initialize Instaloader instance
    video_file_path = None  # Initialize video path variable

    try:
        if "instagram.com/reel/" in reel_url:
            shortcode = reel_url.split("instagram.com/reel/")[1].split("/")[0]
        else:
            raise ValueError("Invalid Instagram reel URL")

        print(f"Downloading reel: {shortcode}")
        post = instaloader.Post.from_shortcode(loader.context, shortcode)  # Fetch the Instagram post
        loader.download_post(post, target=download_folder)  # Download the video

        # Locate the downloaded video file
        for root, dirs, files in os.walk(download_folder):
            for file_name in files:
                if file_name.endswith(".mp4"):
                    video_file_path = os.path.join(root, file_name)
                    break

        if video_file_path:
            print("Reel downloaded successfully!")
            return video_file_path
        else:
            raise FileNotFoundError("Video file not found in downloaded files.")
    except Exception as e:
        print(f"Error downloading reel: {e}")
        return None


# Step 3: Upload video to pre-signed URL
def upload_video(upload_url, video_file_path):
    """
    Uploads a video to the pre-signed URL.

    Args:
        upload_url (str): Pre-signed URL for uploading.
        video_file_path (str): Path to the video file.

    Returns:
        bool: True if the upload is successful, False otherwise.
    """
    try:
        print(f"Uploading video to {upload_url}...")
        with open(video_file_path, "rb") as video_file:  # Open video file in binary read mode
            headers = {
                "Content-Type": "video/mp4"  # Set content type to video
            }
            response = requests.put(upload_url, headers=headers, data=video_file)  # PUT request to upload video

        if response.status_code == 200:
            print("Video uploaded successfully!")
            return True
        else:
            print(f"Failed to upload video. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error uploading video: {e}")
        return False


# Step 4: Create post with the uploaded video
def create_post(title, video_hash, category_id=25, is_available_in_public_feed=False):
    """
    Creates a post with the uploaded video using its hash.

    Args:
        title (str): The title of the post.
        video_hash (str): The hash of the uploaded video.
        category_id (int): ID of the category (default is 25).
        is_available_in_public_feed (bool): Whether the post should be visible in the public feed.

    Returns:
        None
    """
    try:
        headers = {
            "Flic-Token": FLIC_TOKEN,
            "Content-Type": "application/json"
        }
        data = {
            "title": title,
            "hash": video_hash,
            "is_available_in_public_feed": is_available_in_public_feed,
            "category_id": category_id
        }
        # Create the post via POST request
        response = requests.post(f"{BASE_URL}/posts", headers=headers, json=data)

        if response.status_code == 200:
            print("Post created successfully!")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed to create post. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error creating post: {e}")


# Main execution logic
if __name__ == "__main__":
    """
    Main function to execute the Instagram reel download, video upload, and post creation.
    """
    try:
        # User input for Instagram reel URL, title, and category ID
        reel_url = input("Enter the Instagram reel URL: ").strip()
        video_title = input("Enter a title for the video: ").strip()
        category_id = int(input("Enter a category ID (default is 25): ").strip() or 25)

        # Step 1: Download the reel
        video_file_path = download_instagram_reel(reel_url)

        if video_file_path:
            # Step 2: Get the pre-signed URL and video hash
            upload_url, video_hash = get_upload_url()

            if upload_url and video_hash:
                # Step 3: Upload the video
                if upload_video(upload_url, video_file_path):
                    # Step 4: Create a post with the uploaded video
                    create_post(video_title, video_hash, category_id)
        else:
            print("Failed to download the Instagram reel.")
    except Exception as e:
        print(f"Error in the main execution: {e}")
