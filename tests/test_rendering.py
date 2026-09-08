import pytest

from math_mcp.tools.rendering import plot_function, plot_implicit, render_math, to_latex
from mcp.types import ImageContent


@pytest.mark.asyncio
async def test_to_latex_returns_latex_and_rendering() -> None:
    result = await to_latex("sin(x)/x")

    assert isinstance(result, ImageContent)


@pytest.mark.asyncio
async def test_render_math_returns_image_content() -> None:
    result = await render_math(r"\int_0^1 x^2\,dx = \frac{1}{3}")
    assert isinstance(result, ImageContent)


@pytest.mark.asyncio
async def test_plot_function_returns_image_content() -> None:
    result = await plot_function(["sin(x)", "cos(x)"], x_range=[-3.14, 3.14], num_points=200)
    assert isinstance(result, ImageContent)


@pytest.mark.asyncio
async def test_plot_implicit_returns_image_content() -> None:
    result = await plot_implicit("x**2 + y**2 = 1", x_range=[-2, 2], y_range=[-2, 2], grid_size=100)
    assert isinstance(result, ImageContent)
