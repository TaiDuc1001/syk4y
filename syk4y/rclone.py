import os
try:
    import gdown
except ImportError:
    print("gdown module not found. Install it using 'pip install gdown'.")
    os.system("pip install gdown")

import gdown

def install_rclone(config_key, rclone_root=None):
    if rclone_root is None:
        rclone_root = os.path.expanduser('~/.config/rclone')
    os.system(f'gdown --fuzzy {config_key}')
    os.system('curl https://rclone.org/install.sh | bash')
    os.system('rclone config file')
    os.system(f'mv rclone.conf {rclone_root}/')
    print('Rclone installed successfully. Rclone configuration file moved to:', os.path.join(rclone_root, 'rclone.conf'))

def rclone_get_remotes():
    remotes = os.popen('rclone listremotes').read().strip().split('\n')
    if remotes == ['']:
        print("No remotes found. Please configure rclone first.")
    else:
        print("Available remotes:")
        for remote in remotes:
            print(remote.strip())

def rclone_copy(source, destination):
    print("""
        Destination format is: remote_name:path/to/destination
        In google drive, the path will be: folder/subfolder/file.txt
        The remote_name you can get from rclone_get_remotes()
        Example: rclone_copy('local_file.txt', 'remote_name:folder/subfolder/file.txt')
        Or: rclone_copy('remote_name:path/to/source', 'path/to/destination')
    """)
    os.system(f'rclone copy {source} {destination}')

if __name__ == "__main__":
    # Example usage
    # Replace 'your_config_key' with the actual key for your rclone config file
    url = 'https://drive.google.com/uc?id=your_config_key'
    config_key = url.split('id=')[-1]
    install_rclone(config_key)
    # rclone_get_remotes()
    # rclone_copy('local_file.txt', 'remote_name', 'destination_path')