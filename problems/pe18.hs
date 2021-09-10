maxPath (x:y:xs) = maxPath (z:xs)
	where z = zipWith (+) (zipWith max x (tail x)) y
maxPath [[x]] = x

convert = map (map read . words)
prob67 = show . maxPath . reverse . convert . lines

main = readFile "./inputs/input18.txt" >>= putStrLn . prob67