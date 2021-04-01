function digitalroot(n)
    ns = string(n)
    sum = 0
    for i in ns
      sum += (Int(i) - Int('0'))
    end
    if(sum > 9)
      return digitalroot(sum)
    else
      return sum
    end
 end