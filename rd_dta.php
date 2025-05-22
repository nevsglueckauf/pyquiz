<?php
/***
 * Little helper for documenation:
 * 
 *  - scanning dir
 *  - creating Markdown and / or HTML code snippets
 * 
 * @since 2025-05-22
 * @author Sven Schrodt 
 */


 /**
 * File system scanner 
 */
class FsScanner
{
    private $current = [];
    private $filtered = [];

    public function dir(string $dirName='.', bool $skipDotFiles = true, int $sortOrder = SCANDIR_SORT_ASCENDING): self
    {
        $tmp = scandir($dirName,$sortOrder);
        if ($skipDotFiles) {
            $dots[] = array_search('.', $tmp, true);
            $dots[] = array_search('..', $tmp, true);
            unset($tmp[$dots[0]]);
            unset($tmp[$dots[1]]);
        }
        $this->current = $tmp;
        return $this;
    }

    public function filterByExt(string $ext='md'): self
    {
        $this->filtered =  array_filter($this->current, function($item) use ($ext) {
            if(str_ends_with($item, '.'.$ext)) return true;
        });
        return $this;
    }

    public function filtered(): array
    {
         if(!count($this->filtered)) $this->filtered = $this->current;
        return $this->filtered;
    }

    public function mdLink(): string
    {
        $tmp = [];
       

        foreach($this->filtered() as $item) {
            $uri = $item;
            $txt = $uri;
            $tmp[] = "[$txt]($uri)";
        }

        return implode(separator: PHP_EOL, array: $tmp);
    }
}
$dirname = 'doq';
$scanner = new FsScanner();
$rs = $scanner->dir(dirName:$dirname, sortOrder:SCANDIR_SORT_NONE)->filterByExt('md')->mdLink();

#filterByExt($dirname)->mdLink();
print_r($rs);