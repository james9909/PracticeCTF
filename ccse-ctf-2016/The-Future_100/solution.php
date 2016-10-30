<?php

$first = 391220580;

$time = 1477459467;
while (true) {
    mt_srand(($time - 42) ^ 42);
    $rand0 = mt_rand();
    if ($rand0 === $first) {
        $rand1 = mt_rand();
        $rand2 = mt_rand();
        print $rand2;
        break;
    }
    $time += 1;
}

?>
