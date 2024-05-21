#
# SPDX-License-Identifier: CC-BY-NC-ND-4.0
#
# revision-save-storage-wrapper
# Copyright (c) 2024 Patrick Wilmes <p.wilmes89@gmail.com>
#
# This file is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://creativecommons.org/licenses/by-nc-nd/4.0/
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


#!/usr/bin/env python
import os
import click
import subprocess


@click.group()
def cli():
    """A simple CLI wrapper for Git."""
    pass


@cli.command()
def init():
    """Initialize a new Git repository."""
    subprocess.run(['git', 'init'])


@cli.command()
@click.argument('message')
def commit(message):
    """Commit changes with a message."""
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', message])


@cli.command()
@click.argument('branch_name')
def branch(branch_name):
    """Create a new branch."""
    subprocess.run(['git', 'checkout', '-b', branch_name])


@cli.command()
def status():
    """Check the status of the repository."""
    subprocess.run(['git', 'status'])


@cli.command()
@click.argument('branch_name')
def checkout(branch_name):
    """Switch to a different branch."""
    subprocess.run(['git', 'checkout', branch_name])


@cli.command()
@click.argument('branch_name')
def merge(branch_name):
    """Merge a branch into the current branch."""
    subprocess.run(['git', 'merge', branch_name])


if __name__ == '__main__':
    cli()

