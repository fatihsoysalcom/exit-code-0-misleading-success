# Exit Code 0 Misleading Success

This example demonstrates how a program can exit with code 0, traditionally signaling success, even when its internal operations did not fully achieve the intended goal. It simulates a file processing script that reports an internal failure (file not found) via standard error, but still returns an exit code of 0 to the operating system. This highlights the article's point that exit code 0 can be a weak indicator of true success.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run from your terminal, then check the exit code:
   - `python main.py existing_file.txt ; echo $?` (This will create 'existing_file.txt' and report success)
   - `python main.py non_existing_file.txt ; echo $?` (This will report a warning to stderr, but still exit 0)

## Original Article

This example accompanies the Turkish article: [Exit Code 0: Başarının En Zayıf Kanıtı](https://fatihsoysal.com/blog/exit-code-0-basarinin-en-zayif-kaniti/).

## License

MIT — see [LICENSE](LICENSE).
