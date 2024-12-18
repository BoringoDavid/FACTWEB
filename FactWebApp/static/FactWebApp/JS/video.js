document.addEventListener('DOMContentLoaded', () => {
    // Select all video elements after DOM is loaded
    const videos = document.querySelectorAll('video');

    // Function to handle video hover effect (play on hover, no sound)
    videos.forEach(video => {
        // Play video on hover
        video.addEventListener('mouseover', () => {
            video.play();
            video.muted = true; // Mute the video on hover
        });

        // Pause video when hover ends
        video.addEventListener('mouseout', () => {
            video.pause();
            video.currentTime = 0; // Reset video to start
        });

        // On click, open the video in an expanded screen (modal view)
        video.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent default behavior (e.g., opening in new tab)

            // Create a div for the modal container
            const modal = document.createElement('div');
            modal.classList.add('modal');  // Adding a class for easier styling
            modal.style.position = 'fixed';
            modal.style.top = '0';
            modal.style.left = '0';
            modal.style.width = '100%';
            modal.style.height = '100%';
            modal.style.background = 'rgba(0, 0, 0, 0.8)';
            modal.style.display = 'flex';
            modal.style.justifyContent = 'center';
            modal.style.alignItems = 'center';
            modal.style.zIndex = '9999';

            // Create a video element for the modal
            const modalVideo = document.createElement('video');
            modalVideo.src = video.src; // Ensure the correct video is opened
            modalVideo.controls = true;
            modalVideo.style.maxWidth = '90%'; // Responsive size
            modalVideo.style.maxHeight = '90%'; // Keep aspect ratio intact
            modalVideo.style.borderRadius = '8px'; // Optional: to match the style

            // Append modal video and modal container to the body
            modal.appendChild(modalVideo);
            document.body.appendChild(modal);

            // Play the video in the modal
            modalVideo.play();

            // Close modal when clicked outside the video or on the modal container
            modal.addEventListener('click', (event) => {
                if (event.target === modal) {
                    document.body.removeChild(modal);
                }
            });
        });
    });

    // Disable simultaneous video play on the same page
    videos.forEach(video => {
        video.addEventListener('play', () => {
            videos.forEach(otherVideo => {
                if (otherVideo !== video) {
                    otherVideo.pause();
                    otherVideo.currentTime = 0; // Reset the video
                }
            });
        });
    });
});
