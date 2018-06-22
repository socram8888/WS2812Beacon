// Copyright 2018 Marcos Del Sol Vives
// SPDX-License-Identifier: ISC

// Tweak these parameters to your hearth's content

// Hole width. Slightly less than led_length minus twice wall_thickness.
hole_width = 33 - 2 * 3 - 0.1;

// Hole length. For this, actually the same as the width.
hole_length = hole_width;

// Hole height. This is the height of the tab that fits in the hole.
hole_height = 3;

// Size of the tabs around the cover, to prevent the cover from going in.
tab_size = 4;

// Height of the tabs.
tab_height = 2;

// END OF CONFIGURATION

cube([hole_width + 2 * tab_size, hole_length + 2 * tab_size, tab_height]);
translate([tab_size, tab_size, tab_height])
    cube([hole_width, hole_length, hole_height]);
