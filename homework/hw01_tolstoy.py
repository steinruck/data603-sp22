{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "hw01-tolstoy.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPdgC9/iaaugSEPYJU+QEUM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/steinruck/data603-sp22/blob/class/homework/hw01_tolstoy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Assignment: write a script that calculates the number of unique words in Tolstoy’s War and Peace\n",
        "\n",
        "### Step 1: Import Modules"
      ],
      "metadata": {
        "id": "TKom4bey7Cn7"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "8GCT-MqRYras"
      },
      "outputs": [],
      "source": [
        "from urllib import request\n",
        "import re "
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Step 2: Read Into Variable From URL\n",
        "  - open the url and decode each line into a list"
      ],
      "metadata": {
        "id": "Vysi1M6X7mCd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "url = 'https://www.gutenberg.org/files/2600/2600-0.txt'\n",
        "file = request.urlopen(url)\n",
        "\n",
        "text_list = [line.decode('utf-8') for line in file]"
      ],
      "metadata": {
        "id": "7nt6PB1KZuwK"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Step 3: Create Cleaning Function\n",
        "  - Turn list into string\n",
        "  - split string into list of words\n",
        "  - make everything lowercase\n",
        "  - remove special characters\n",
        "  - remove numbers\n",
        "  - convert all spaces to single space\n",
        "  - remove empty lines"
      ],
      "metadata": {
        "id": "EDATdNVo7-_P"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def clean(text_list):\n",
        "  # flatten the list\n",
        "  joined = ' '.join(text_list)\n",
        "\n",
        "  # split by word\n",
        "  text = joined.split(' ')\n",
        "\n",
        "  # make everything lowercase\n",
        "  lowercase = [i.lower() for i in text]\n",
        "\n",
        "  # remove special characters\n",
        "  symbol = [re.sub('\\W',\" \", line) for line in lowercase]\n",
        "\n",
        "  # remove numbers\n",
        "  numbers = [re.sub('\\d+',\" \", line) for line in symbol]\n",
        "\n",
        "  # make spaces single space\n",
        "  whitespace = [re.sub('\\s+',\"\", line) for line in numbers]\n",
        "\n",
        "  # remove empty lines if there are any\n",
        "  empty = [line for line in whitespace if line]\n",
        "  return empty "
      ],
      "metadata": {
        "id": "XkF5fJQVbwIc"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Step 4: Send Text Through Cleaning Function\n",
        "  - run function with text_list as input\n",
        "  - convert list to set because set only keeps one instance of each item\n",
        "  - find length of set"
      ],
      "metadata": {
        "id": "NVA2jYu38jPl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# store output of function as a variable\n",
        "cleaned = clean(text_list)\n",
        "\n",
        "# convert list to set because sets only contain unique values\n",
        "unique = set(cleaned)\n",
        "\n",
        "# length of a set is the number of unique words\n",
        "print(\"There are \" + str(len(unique)) + \" unique words in this text.\")"
      ],
      "metadata": {
        "id": "nLIJ8iQwj6bk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ce4ac17e-ff83-4ee5-c598-68f20c9d197a"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "There are 20332 unique words in this text.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Furthur efforts\n",
        "If we're looking only for the counts of the words in the actual book and not the editors notes or anything else, must first remove those. SO:\n",
        "- Remove everything up to the beginning of the first chapter\n",
        "  - title page, copyright info, table of contents, end comments, etc\n",
        "  - Book 1 starts at line 827 and the content ends 352 lines from the end where legal notice begins\n",
        "    - trial and error. Just sliced until I found the right start/stop"
      ],
      "metadata": {
        "id": "y9VyoNLEI4pj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# save only the items between these indices\n",
        "just_text = text_list[827:-352]"
      ],
      "metadata": {
        "id": "S5EyH7-BJLOZ"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "clean_text = clean(just_text)\n",
        "\n",
        "new_unique = set(clean_text)\n",
        "print(\"There are \" + str(len(new_unique)) + \" unique words after removing publishing additions.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m5PBURdCeHoQ",
        "outputId": "ec0c289e-3ed9-4b49-b8f8-f703079ae203"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "There are 20171 unique words after removing publishing additions.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Not a big difference but there is a difference"
      ],
      "metadata": {
        "id": "G-ZFovTnOzXC"
      }
    }
  ]
}