if False:
    print('true is true')

if 10 > 5:
    print('ten is greater than five')

is_cold_outside = True
is_windy = False

if is_cold_outside or is_windy:
    print('wear a jacket')

if is_cold_outside and is_windy:
    print('wear a jacket and a windbreaker')
elif is_cold_outside:
    print('wear a jacket')
elif is_windy:
    print('wear a windbreaker')
else:
    print('summer clothes!')

has_red_paint = True
has_blue_paint = True

if has_red_paint and has_blue_paint:
    print('painting in purple')
elif has_red_paint:
    print('painting in red')
elif has_blue_paint:
    print('painting in blue')
else:
    print('not painting')

if has_red_paint:
    print('painting in red')
if has_blue_paint:
    print('painting in blue')
