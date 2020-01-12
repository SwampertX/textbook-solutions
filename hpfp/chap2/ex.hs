-- ex.hs

-- z = 7
-- x = y ^ 2
-- waxOn = x * 5
-- y = z + 8

-- q4

waxOn = x * 5
    where x = y ^ 2
          z = 7
          y = z + 8

-- q5
triple x = x * 3

-- q6
-- waxOff x = triple x

-- q7
waxOff x = (^2) $ 3 * x
