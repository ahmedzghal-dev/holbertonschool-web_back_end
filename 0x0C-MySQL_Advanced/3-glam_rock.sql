-- SQL script that lists all bands with Glam rock as their main style
-- following these requirements
SELECT band_name, IFNULL(split, 2023) - IFNULL(formed, 0) AS lifespan
From metal_bands  WHERE style LIKE '%Glam rock%';