#Define the dimensions of the background panels
panelX = 1
panelY = 1
panelZ = 1

# 3D coordinate to background image mapping
background_map = {
    (0, 0, 0): "Images\\Backgrounds\\bg_000.png",
    (1, 0, 0): "Images\\Backgrounds\\bg_100.png",
    (2, 0, 0): "Images\\Backgrounds\\bg_010.png",
    (3, 0, 0): "Images\\Backgrounds\\bg_110.png",
    (4, 0, 0): "Images\\Backgrounds\\bg_001.png",
    (5, 0, 0): "Images\\Backgrounds\\bg_101.png",
    (6, 0, 0): "Images\\Backgrounds\\bg_011.png",
    (7, 0, 0): "Images\\Backgrounds\\bg_111.png",
    (8, 0, 0): "Images\\Backgrounds\\bg_000.png",
    (9, 0, 0): "Images\\Backgrounds\\bg_100.png",
    (10, 0, 0): "Images\\Backgrounds\\bg_010.png",
}

def get_image_path(x, y, z):
    #Get background image path based on X, Y, Z coordinates.
    coords = (x, y, z)
    return background_map.get(coords, "Images\Backgrounds\download.png")  # fallback image

image_path = get_image_path(panelX, panelY, panelZ)