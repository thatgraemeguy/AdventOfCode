#!/usr/bin/awk -f

BEGIN {
	e=1
}

{
	if ($0 == "")
		e++
	else
		elves[e] += $0
}

END {
	n = asort(elves)
	print "Part 1:", elves[n]
	print "Part 2:", elves[n]+elves[n-1]+elves[n-2]
}

