# YaDisk-Dup-Cleaner
The program deletes obsolete files on Yandex disk. Files should have the structure: &lt;timestamp&gt;\_&lt;id&gt;_&lt;name&gt;, where &lt;timestamp&gt; is a time branch, &lt;id&gt; is a unique identifier, &lt;name&gt; is the remaining part of the name.

# Instructions for use

1. Clone the repository as follows:
```bash
git clone https://github.com/Larionov-VA/YaDisk-Dup-Cleaner.git
```

2. Go to the directory with the project code:
```bash
cd YaDisk-Dup-Cleaner/src
```

3. Create an environment variable and activate it:
```bash
python3 -m venv .venv && source .venv/bin/activate
```

4. Install the necessary dependencies:
```bash
pip -r requirements.txt
```

5. Run cleanup like this:
```bash
python3 main.py -t \<Your_OAuth_token\> -f \<Folder_name\>
```