<?php

$i = 0;
$line_of_poem = array();
$corpus = array();
$corpus_content = array();
$corpus_poetry_by_line = array();

# import file names for all txt files in the folder
foreach (scandir('./') as $key => $file_name) {
  if (strpos($file_name, '.txt') !== false) {
    $corpus[] = $file_name;
  }
}

# read in the text from each text file as a list of lines
# with new line characters stripped
foreach($corpus as $key => $poem) {
  $poem_text = @fopen('./' . $poem, 'r');
  $corpus_content[$poem] = file('./' . $poem);
  }


# create a dictionary in which each key is a line number (starting with zero, because Python
# and each value is a list of lines, one from each imported poem
while ($i < 77) {
  $single_line_content_all_poems = array();
  foreach($corpus as $key => $poem) {
    $single_line_content_all_poems[] = $corpus_content[$poem][$i];
  }
  $corpus_poetry_by_line[$i] = $single_line_content_all_poems;
  $i++;
}

# assemble a new poem that takes one random version of each line
$assembled_poem = array();
foreach($corpus_poetry_by_line as $key => $line) {
  $random_key = array_rand(array_values($line), 1);
  $assembled_poem[] = $line[$random_key];
  $i++;
}

# print the newly created poem
foreach($assembled_poem as $line) {
  $chars = str_split($line);
  $line_out = '';
  foreach($chars as $index => $char) {
    if ($char == '|') {
      $line_out .= '\n';
    } else {
      $line_out .= $char;
    }
  }
  print($line_out);
}

/*
foreach($assembled_poem as $index => $line) {
  echo $line;
}
*/
?>
