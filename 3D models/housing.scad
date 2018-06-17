// Copyright 2018 Marcos Del Sol Vives
// SPDX-License-Identifier: ISC

// Tweak these parameters to your hearth's content

// Rendering quality
$fn = 20;

// Length of *each* side of the LED
led_length = 33;

// Height of the LED strip
led_height = 12;

// Thickness of the LED strip, at the max spot
led_thickness = 3;

// Height of the tabs that hold the glass
glass_support_height = 3;

// Thickness of the glass
glass_thickness = 3;

// Thickness of the bezel on top and on the bottom, protecting the edges of the glass
bezel_height = 3;

// Thickness of the walls
wall_thickness = 3;

// Thickness of the hole to pass the cabling to the strip
cable_thickness = 1.5;

// Support stick hole depth
support_depth = 11;

// Diameter of the support stick
support_diam = 6;

// DC jack hole
dc_jack_pos_x = 0.35;
dc_jack_pos_y = 0.65;
dc_jack_diam = 8.2;

// END OF CONFIGURATION

totalheight = led_height + 2 * glass_support_height + 2 * bezel_height;
totalside = led_length + 2 * led_thickness + 2 * glass_thickness;

difference() {
    union() {
        difference() {
            union() {
                // Bottom bezel
                cube([totalside, totalside, bezel_height]);

                // Bottom glass support
                translate([glass_thickness, glass_thickness, bezel_height])
                    cube([led_length + 2 * led_thickness, led_length + 2 * led_thickness, glass_support_height]);

                // LED support
                translate([glass_thickness + led_thickness, glass_thickness + led_thickness, bezel_height + glass_support_height])
                    cube([led_length, led_length, led_height]);

                // Top glass support
                translate([glass_thickness, glass_thickness, bezel_height + glass_support_height + led_height])
                    cube([led_length + 2 * led_thickness, led_length + 2 * led_thickness, glass_support_height]);

                // Top bezel
                translate([0, 0, bezel_height + glass_support_height + led_height + glass_support_height])
                    cube([totalside, totalside, bezel_height]);
            };
            
            // Make it hollow to fit the driver inside
            translate([glass_thickness + led_thickness + wall_thickness, glass_thickness + led_thickness + wall_thickness, wall_thickness]) {
                cube([led_length - 2 * wall_thickness, led_length - 2 *wall_thickness, totalheight - wall_thickness]);
            };

            // Make hole for the LED cable
            translate([glass_thickness + led_thickness + led_length - wall_thickness - cable_thickness, glass_thickness + led_thickness, bezel_height + glass_support_height])
                cube([cable_thickness, wall_thickness, led_height]);
        };

        // Support part
        translate([glass_thickness + led_thickness + wall_thickness, glass_thickness + led_thickness + wall_thickness, 0])
            cube([support_diam + wall_thickness, support_diam + wall_thickness, support_depth + wall_thickness]);
    };

    // Hole in support
    translate([glass_thickness + led_thickness + wall_thickness + support_diam / 2, glass_thickness + led_thickness + wall_thickness + support_diam / 2, 0])
        cylinder(d=support_diam, h=support_depth);

    // Hole for DC jack
    translate([totalside * dc_jack_pos_x, totalside * dc_jack_pos_y, 0])
        cylinder(d=dc_jack_diam, h=wall_thickness);
};