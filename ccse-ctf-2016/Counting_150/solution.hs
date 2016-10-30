main = do
    let list = [1 | x <- [0..687], y <- [0..687], z <- [0..687], x+y+z < 687]
    print (length list)
