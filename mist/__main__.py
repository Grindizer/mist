#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import click
from mist import adapt_to_provider

@click.group()
@click.option('--dont-show', required=False, type=click.BOOL, default=False)
@click.option('--filename', required=False, type=click.Path(exists=False))
@click.option('--format', required=False, default='png', type=click.Choice(['png', 'jpeg', 'pdf', 'svg']))
@click.option('--engine', required=False, default='dot', type=click.Choice(['dot', 'fdp', 'neato']))
@click.pass_context
def main(ctx, dont_show, filename, format, engine):
    pass


@main.command("deis")
@click.option('-h', '--endpoint', required=True,
              help=u"deis cluster endpoint")
@click.option('-u', '--username', required=True,
              help=u"deis user for login")
@click.option('-p', '--password', required=True,
              help=u"deis password")
@click.pass_context
def deis(ctx, endpoint, username, password):
    graph = adapt_to_provider('deis', dict(
        endpoint=endpoint,
        username=username,
        password=password,
    ))
    graph.format = ctx.parent.params['format']
    graph.engine = ctx.parent.params['engine']
    graph.render(filename=ctx.parent.params['filename'], view=not ctx.parent.params['dont_show'], cleanup=True)

if __name__ == '__main__':
    main()