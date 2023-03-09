-- SQL script that lists all bands with Glam rock as their main style
-- following these requirements
SELECT band_name, (split - formed) AS lifespan
From metal_bands  WHERE style = 'Glam rock' ORDER BY lifespan DESC;