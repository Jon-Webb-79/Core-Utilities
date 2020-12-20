# Import necessary packages here
from typing import List
import warnings
from matplotlib import rc, pyplot as plt
# ============================================================================
# ============================================================================
# Date:    December 18, 2020
# Purpose: This file contains classes and functions necessary for
#          plotting.

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2020, Jon Webb Inc."
__version__ = "1.0"
# ============================================================================
# ============================================================================


def two_d_line_matplot(x_data: List[List[float]], y_data: List[List[float]],
                       line_colors: List[str], line_style: List[str],
                       line_weight: List[str], x_label: str, y_label: str,
                       dat_labels: List[str], label_pos: str, x_scale: str = 'LIN',
                       y_scale: str = 'LIN', plot_name: str = 'NULL',
                       save: bool = False, label_font_size: int = 18,
                       tick_font_size: int = 18, style_name: str = 'default') -> None:
    """

    :param x_data: A list of lists, where the inner lists contain data points
                   for the x-axis
    :param y_data: A list of lists, where the inner lists contain data points
                   for the y-axis
    :param line_colors: A list of line colors ,one for each curve.
                    Acceptable line color indicators can be found in documentation
                    for
                    matplotlib colors <https://matplotlib.org/3.1.0/gallery/color/named_colors.html>`_.
    :param line_style: A list of line styles, one for each curve.  Acceptable line
                    styles can be found in documentation for
                    `matplotlib style <https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html>`_.
    :param line_weight: A list of line weights, one for each curve.
    :param x_label: The label for the x-axis
    :param y_label: The label for the y-axis
    :param dat_labels: A list of labels, one for each curve
    :param label_pos: The position of the label in the plot, examples might be
                      ``upper left``, ``lower right``.
    :param x_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param y_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param plot_name: The plot name and path-link, if the user wants to save the
                      plot.  If not, the variable is defaulted to ``NULL``
    :param save: True or False, defaulted to False
    :param label_font_size: The font size for plot labels, defaulted to 18
    :param tick_font_size: The tick font size, defaulted to 18
    :param style_name: The plot style to be used.  Acceptable styles can be
                found at
                `matplotlib styles <https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html>`_.
                defaulted to ``default``
    :return None:

    This function utilizes the matplotlib
    `subplots <https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html>`_ functionality
    to produce single plots of one or multiple data sets.  This function will only produce line plots and
    not scatter plots or a combination of both.  The function can be used in the following manner;

    .. code-block:: python

       > x_dat = np.linspace(0, 10, 15)
       > y1_dat = x_dat
       > y2_dat = x_dat ** 2.0
       > y3_dat = x_dat ** 3.0
       > x_list = [x_dat, x_dat, x_dat]
       > y_list = [y1_dat, y2_dat, y3_dat]
       > colors = ['red', 'blue', 'black']
       > line_style = ['-', '-', '--']
       > labels = ['linear', 'squared', 'cubed']
       > weight = [1, 2, 3]
       > two_d_line_matplot(x_list, y_list, colors, line_style, weight, 'x-data',
                            'y-data', labels, 'upper left')

    .. image:: line_plot.eps
       :scale: 90%
       :align: center

    """
    # Error checking and warnings
    if save and plot_name == 'NULL':
        warnings.warn('if save is True then plot name cannot be NULL')
    if len(x_data) != len(y_data):
        warnings.warn('length of x list of lists is not the same as y list of lists, plot not printed')
        return
    if len(line_colors) != len(x_data):
        warnings.warn('line colors list not the same length as data lists, plot not printed')
        return
    if len(line_style) != len(x_data):
        warnings.warn('line_style list not the same length as data lists, plot not printed')
        return
    if len(line_weight) != len(x_data):
        warnings.warn('line_weight list not the same length as data lists, plot not printed')
        return
    if y_scale != 'LOG' and y_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')
    if x_scale != 'LOG' and x_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')

    # begin plot
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use(style_name)
    fig, td_plot = plt.subplots()
    rc('xtick', labelsize=tick_font_size)
    rc('ytick', labelsize=tick_font_size)
    td_plot.set_xlabel(x_label, fontsize=label_font_size)
    td_plot.set_ylabel(y_label, fontsize=label_font_size)
    if x_scale.upper() == 'LOG':
        td_plot.set_xscale('log')
    if y_scale.upper() == 'LOG':
        td_plot.set_yscale('log')

    for i in range(len(line_colors)):
        td_plot.plot(x_data[i], y_data[i], color=line_colors[i],
                     label=dat_labels[i], linewidth=line_weight[i],
                     linestyle=line_style[i])

    plt.legend(loc=label_pos)
    if not save:
        plt.show()
    else:
        plt.savefig(plot_name)
# ----------------------------------------------------------------------------


def two_d_scatter_matplot(x_data: List[List[float]], y_data: List[List[float]],
                          marker_colors: List[str], marker_style: List[str],
                          x_label: str, y_label: str, dat_labels: List[str],
                          label_pos: str, x_scale: str = 'LIN',
                          y_scale: str = 'LIN', plot_name: str = 'NULL',
                          save: bool = False, label_font_size: int = 18,
                          tick_font_size: int = 18, style_name: str = 'default') -> None:
    """

    :param x_data: A list of lists, where the inner lists contain data points
                   for the x-axis
    :param y_data: A list of lists, where the inner lists contain data points
                   for the y-axis
    :param marker_colors: A list of line colors ,one for each curve.
                          Acceptable line color indicators can be found in documentation
                          for `matplotlib colors <https://matplotlib.org/3.1.0/gallery/color/named_colors.html>`_.
    :param marker_style: A list of line styles, one for each curve.  Acceptable line
                         styles can be found in documentation for `matplotlib style`_.
    :param x_label: The label for the x-axis
    :param y_label: The label for the y-axis
    :param dat_labels: A list of labels, one for each curve
    :param label_pos: The position of the label in the plot, examples might be
                      ``upper left``, ``lower right``
    :param x_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param y_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param plot_name: The plot name and path-link, if the user wants to save the
                      plot.  If not, the variable is defaulted to ``NULL``
    :param save: True or False, defaulted to False
    :param label_font_size: The font size for plot labels, defaulted to 18
    :param tick_font_size: The tick font size, defaulted to 18
    :param style_name: The plot style to be used.  Acceptable styles can be
                       found at
                `matplotlib styles <https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html>`_.
                       defaulted to ``default``
    :return None:

    This function utilizes the matplotlib
    `subplots <https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html>`_ functionality
    to produce single plots of one or multiple data sets.  This function will only produce line plots and
    not scatter plots or a combination of both.  The function can be used in the following manner;

    .. code-block:: python

       > x_dat = np.linspace(0, 10, 15)
       > y1_dat = x_dat
       > y2_dat = x_dat ** 2.0
       > y3_dat = x_dat ** 3.0
       > x_list = [x_dat, x_dat, x_dat]
       > y_list = [y1_dat, y2_dat, y3_dat]
       > colors = ['red', 'blue', 'black']
       > line_style = ['-', '-', '--']
       > labels = ['linear', 'squared', 'cubed']
       > weight = [1, 2, 3]
       > two_d_scatter_matplot(x_list, y_list, colors, line_style, weight, 'x-data',
                               'y-data', labels, 'upper left')

    .. image:: scatter_plot.eps
       :align: center

    """
    # Error checking and warnings
    if save and plot_name == 'NULL':
        warnings.warn('if save is True then plot name cannot be NULL')
    if len(x_data) != len(y_data):
        warnings.warn('length of x list of lists is not the same as y list of lists, plot not printed')
        return
    if len(marker_colors) != len(x_data):
        warnings.warn('line colors list not the same length as data lists, plot not printed')
        return
    if len(marker_style) != len(x_data):
        warnings.warn('line_style list not the same length as data lists, plot not printed')
        return
    if y_scale != 'LOG' and y_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')
    if x_scale != 'LOG' and x_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')

    # begin plot
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use(style_name)
    fig, td_plot = plt.subplots()
    rc('xtick', labelsize=tick_font_size)
    rc('ytick', labelsize=tick_font_size)
    td_plot.set_xlabel(x_label, fontsize=label_font_size)
    td_plot.set_ylabel(y_label, fontsize=label_font_size)
    if x_scale.upper() == 'LOG':
        td_plot.set_xscale('log')
    if y_scale.upper() == 'LOG':
        td_plot.set_yscale('log')

    for i in range(len(marker_colors)):
        td_plot.plot(x_data[i], y_data[i], color=marker_colors[i],
                     label=dat_labels[i], marker=marker_style[i],
                     linestyle=' ')

    plt.legend(loc=label_pos)
    if not save:
        plt.show()
    else:
        plt.savefig(plot_name)
# ----------------------------------------------------------------------------


def two_d_scatter_line_matplot(x_data: List[List[float]], y_data: List[List[float]],
                               marker_colors: List[str], marker_style: List[str],
                               line_style: List[str], line_weight: List[str],
                               x_label: str, y_label: str, dat_labels: List[str],
                               label_pos: str, x_scale: str = 'LIN',
                               y_scale: str = 'LIN', plot_name: str = 'NULL',
                               save: bool = False, label_font_size: int = 18,
                               tick_font_size: int = 18, style_name: str = 'default') -> None:
    """

    :param x_data: A list of lists, where the inner lists contain data points
                   for the x-axis
    :param y_data: A list of lists, where the inner lists contain data points
                   for the y-axis
    :param marker_colors: A list of line colors ,one for each curve.
                          Acceptable line color indicators can be found in documentation
                          for `matplotlib colors <https://matplotlib.org/3.1.0/gallery/color/named_colors.html>`_.
    :param marker_style: A list of line styles, one for each curve.  Acceptable line
                         styles can be found in documentation for `matplotlib style`_.
    :param line_style: A list of line styles, one for each curve.  Acceptable line
                    styles can be found in documentation for
                    `matplotlib style <https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html>`_.
    :param line_weight: A list of line weights, one for each curve.
    :param x_label: The label for the x-axis
    :param y_label: The label for the y-axis
    :param dat_labels: A list of labels, one for each curve
    :param label_pos: The position of the label in the plot, examples might be
                      ``upper left``, ``lower right``
    :param x_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param y_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param plot_name: The plot name and path-link, if the user wants to save the
                      plot.  If not, the variable is defaulted to ``NULL``
    :param save: True or False, defaulted to False
    :param label_font_size: The font size for plot labels, defaulted to 18
    :param tick_font_size: The tick font size, defaulted to 18
    :param style_name: The plot style to be used.  Acceptable styles can be
                found at
                `matplotlib styles <https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html>`_.
                defaulted to ``default``
    :return None:

    This function utilizes the matplotlib
    `subplots <https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html>`_ functionality
    to produce single plots of one or multiple data sets overlaid with line plots.  This function will only produce
    line plots and not scatter plots or a combination of both.  The function can be used in the following manner;

    .. code-block:: python

       > x_dat = np.linspace(0, 10, 15)
       > y1_dat = x_dat
       > y2_dat = x_dat ** 2.0
       > y3_dat = x_dat ** 3.0
       > x_list = [x_dat, x_dat, x_dat]
       > y_list = [y1_dat, y2_dat, y3_dat]
       > colors = ['red', 'blue', 'black']
       > line_style = ['-', '-', '--']
       > labels = ['linear', 'squared', 'cubed']
       > weight = [1, 2, 3]
       > marker_style = ['^', 'o', 'd']
       > two_d_scatter_line_matplot(x_list, y_list, colors, marker_style,
                                   line_style, weight, 'x-axis', 'y-axis',
                                   labels, 'upper left', save=True, plot_name=plt_name)

    .. image:: line_mark.eps
       :align: center
    """
    # Error checking and warnings
    if save and plot_name == 'NULL':
        warnings.warn('if save is True then plot name cannot be NULL')
    if len(x_data) != len(y_data):
        warnings.warn('length of x list of lists is not the same as y list of lists, plot not printed')
        return
    if len(marker_colors) != len(x_data):
        warnings.warn('line colors list not the same length as data lists, plot not printed')
        return
    if len(marker_style) != len(x_data):
        warnings.warn('line_style list not the same length as data lists, plot not printed')
        return
    if y_scale != 'LOG' and y_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')
    if x_scale != 'LOG' and x_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')

    # begin plot
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use(style_name)
    fig, td_plot = plt.subplots()
    rc('xtick', labelsize=tick_font_size)
    rc('ytick', labelsize=tick_font_size)
    td_plot.set_xlabel(x_label, fontsize=label_font_size)
    td_plot.set_ylabel(y_label, fontsize=label_font_size)
    if x_scale.upper() == 'LOG':
        td_plot.set_xscale('log')
    if y_scale.upper() == 'LOG':
        td_plot.set_yscale('log')
    for i in range(len(marker_colors)):
        td_plot.plot(x_data[i], y_data[i], color=marker_colors[i],
                     label=dat_labels[i], marker=marker_style[i],
                     linestyle=line_style[i], linewidth=line_weight[i])

    plt.legend(loc=label_pos)
    if not save:
        plt.show()
    else:
        plt.savefig(plot_name)
# ----------------------------------------------------------------------------


def one_d_histogram_plot(data: List[List[float]], labels: List[List[str]],
                         x_label: str, y_label: str, colors: List[str],
                         edge_colors: List[str], shading: List[float],
                         label_pos: str, num_bins: int = 50, tick_font_size: int = 18,
                         label_font_size: str = 18, style_name: str = 'default',
                         save: bool = False, plot_name: str = 'NULL',
                         hist_type: str = 'bar', dens: bool = False) -> None:
    """

    :param data: A list of lists containing data for one or multiple
                 distributions
    :param labels: A list of labels, one for each distribution
    :param x_label: The label for the x-axis
    :param y_label: The label for the y-axis
    :param colors: The fill colors for each ``bar`` plot.  If a ``step`` plot
                   is selected, this input is irrelevant, but data must still be
                   passed to the function.
    :param edge_colors: The colors for the edge of each bar or step plot
    :param shading: The level of transparency for bar plot fill.  a Value of
                    0 is invisible, 1 is the maximum color density
    :param label_pos: Where in the plot, the labels for each curve are to be
                      placed.  ``upper left`` or ``lower right`` are examples.
    :param num_bins: The number of bins to be plotted, defaulted to 50
    :param tick_font_size: The size for each tick, defaulted to 18
    :param label_font_size: The size for printed font, defaulted to 18
    :param style_name: The plot style to be used.  Acceptable styles can be
                found at
                `matplotlib styles <https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html>`_.
                defaulted to ``default``
    :param save: True or False, defaulted to False
    :param plot_name: The plot name and path-link, if the user wants to save the
                      plot.  If not, the variable is defaulted to ``NULL``
    :param hist_type: {``bar``, ``barstacked``, ``step``, ``stepfilled``}
                See
                `histogram <https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html>`_
                for more information.
    :param dens: If True, the first element of the return tuple will be the counts
                 normalized to form a probability density, i.e., the area (or integral)
                 under the histogram will sum to 1
    :return:

    This function utilizes the matplotlib
    `subplots <https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html>`_ functionality
    to produce single plots of one or multiple data sets overlaid with line plots.  This function will only produce
    line plots and not scatter plots or a combination of both.  The function can be used in the following manner;

    .. code-block:: python

       > np.random.seed(19680801)
       > x = np.random.normal(15.0, 3.0, 1000)
       > y = np.random.normal(20.0, 3.0, 1000)
       > data = [x, y]
       > labels = ['one', 'two']
       > colors = ['blue', 'green']
       > edge_colors = ['black', 'black']
       > alpha = [0.9, 0.2]
       > x_label = 'x-axis'
       > y_label = 'y-axis'

       > one_d_histogram_plot(data, labels, x_label, y_label, colors, edge_colors,
                              alpha, 'upper left', num_bins=50, hist_type='step',
                              dens=True)

    .. image:: hist1.eps
       :align: center

    The plot parameters can be changed to produce a normalized plot, only
    showing the histogram outline with the following code.

    .. code-block:: python

       > np.random.seed(19680801)
       > x = np.random.normal(15.0, 3.0, 1000)
       > y = np.random.normal(20.0, 3.0, 1000)
       > data = [x, y]
       > labels = ['one', 'two']
       > colors = ['black', 'red']
       > edge_colors = ['black', 'red']
       > alpha = [1.0, 1.0]
       > x_label = 'x-axis'
       > y_label = 'y-axis'

       > one_d_histogram_plot(data, labels, x_label, y_label, colors, edge_colors,
                              alpha, 'upper left', num_bins=50)

    .. image:: hist2.eps
       :align: center
    """
    if len(labels) != len(data):
        warnings.warn("data list should be the same length as the labels list")
    if len(labels) != len(colors):
        warnings.warn("data list should be the same length as the colors list")
    if len(labels) != len(edge_colors):
        warnings.warn("labels list should be the same length as the edge_colors list")
    if len(labels) != len(shading):
        warnings.warn("labels list should be the same length as the shading list")

    plt.tight_layout()
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use(style_name)
    rc('xtick', labelsize=tick_font_size)
    rc('ytick', labelsize=tick_font_size)
    plt.xlabel(x_label, fontsize=label_font_size)
    plt.ylabel(y_label, fontsize=label_font_size)
    for i in range(len(labels)):
        plt.hist(data[i], bins=num_bins, color=colors[i], edgecolor=edge_colors[i],
                 alpha=shading[i], label=labels[i], histtype=hist_type, density=dens)
    plt.legend(loc=label_pos)
    if not save:
        plt.show()
    else:
        plt.savefig(plot_name)
    plt.close()
# ============================================================================
# ============================================================================
# eof
# TODO Add date plot
